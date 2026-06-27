"""
ClipEquity Core Engine
Description: Tracks content creator clips, viral performance metrics, 
             and calculates automated equity distribution tiers.
"""

class Clipper:
    def __init__(self, username, platform):
        self.username = username
        self.platform = platform
        self.total_views = 0
        self.clips_submitted = 0
        self.equity_tier = "Bronze"
        self.total_payout_earned = 0.0

    def add_clip(self, views):
        """Registers a new clip and updates performance metrics."""
        self.clips_submitted += 1
        self.total_views += views
        self.update_equity_tier()

    def update_equity_tier(self):
        """Dynamically calculates equity tiers based on total views."""
        if self.total_views >= 1000000:
            self.equity_tier = "Diamond"
        elif self.total_views >= 500000:
            self.equity_tier = "Platinum"
        elif self.total_views >= 100000:
            self.equity_tier = "Gold"
        elif self.total_views >= 25000:
            self.equity_tier = "Silver"
        else:
            self.equity_tier = "Bronze"

    def calculate_payout(self, rate_per_thousand):
        """Calculates performance payouts based on cumulative virality."""
        self.total_payout_earned = (self.total_views / 1000) * rate_per_thousand
        return round(self.total_payout_earned, 2)


# --- Simulation Run ---
if __name__ == "__main__":
    print("=== Initializing ClipEquity Trackers ===")
    
    # Create a test creator account
    clipper1 = Clipper(username="PicassoCreate", platform="TikTok")
    
    # Simulate uploading viral clips over time
    print(f"\nRegistering user: {clipper1.username} on {clipper1.platform}")
    
    # Clip 1 goes semi-viral
    print("\n[Clip 1 Uploaded]")
    clipper1.add_clip(views=32000)
    print(f"Total Views: {clipper1.total_views:,} | Tier: {clipper1.equity_tier}")
    
    # Clip 2 hits the algorithm heavy
    print("\n[Clip 2 Uploaded]")
    clipper1.add_clip(views=620000)
    print(f"Total Views: {clipper1.total_views:,} | Tier: {clipper1.equity_tier}")
    
    # Calculate payout calculations based on a $4.50 CPM rate
    payout = clipper1.calculate_payout(rate_per_thousand=4.50)
    print(f"\n=== Financial Settlement ===")
    print(f"Total Payout Allocated: ${payout:,} USD")
